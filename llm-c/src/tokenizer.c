
#include "llm_core.h"
#include <string.h>
#include <ctype.h>

int str_lookup(char* str, Tokenizer* t) {
    // efficiently find the perfect match for str in vocab, return its index or -1 if not found
    for (int i = 0; i < t->vocab_size; i++) {
        if (strcmp(str, t->vocab[i]) == 0) {
            return i;
        }
    }
    return -1;
}

void bpe_encode(char* text, Tokenizer* t, int* tokens, int* n_tokens) {
    // encode the string text (input) into an upper-bound preallocated tokens[] array
    // bpe encode, in principle, repeatedly merges the most frequent pairs
    // in practice, we code this up in a while loop that adds the smallest word first

    // first encode every individual byte in the input string
    *n_tokens = 0; // the number of tokens
    for (char *c = text; *c != '\0'; c++) {
        sprintf(t->str_buffer, "%c", *c);
        int id = str_lookup(t->str_buffer, t);
        if (id != -1) {
            // we found this byte in vocab, add it as a token
            tokens[*n_tokens] = id;
            (*n_tokens)++;
        } else {
            fprintf(stderr, "not all bytes available as tokens, can't encode!\n");
            exit(EXIT_FAILURE);
        }
    }

    // merge the best consecutive pair each iteration, according the scores in vocab_scores
    while (1) {
        float best_score = -1e10;
        int best_id = -1;
        int best_idx = -1;

        for (int i=0; i < (*n_tokens-1); i++) {
            // check if we can merge the pair (tokens[i], tokens[i+1])
            sprintf(t->str_buffer, "%s%s", t->vocab[tokens[i]], t->vocab[tokens[i+1]]);
            int id = str_lookup(t->str_buffer, t);
            if (id != -1 && t->vocab_scores[id] > best_score) {
                // this merge pair exists in vocab! record its score and position
                best_score = t->vocab_scores[id];
                best_id = id;
                best_idx = i;
            }
        }

        if (best_idx == -1) {
            break; // we couldn't find any more pairs to merge, so we're done
        }

        // merge the consecutive pair (best_idx, best_idx+1) into new token best_id
        tokens[best_idx] = best_id;
        // delete token at position best_idx+1, shift the entire sequence back 1
        for (int i = best_idx+1; i < (*n_tokens-1); i++) {
            tokens[i] = tokens[i+1];
        }
        (*n_tokens)--; // token length decreased
    }
}

char* decode(Tokenizer* t, int prev_token, int token) {
    char* piece = t->vocab[token];
    // following BOS (1) token, sentencepiece decoder strips any leading whitespace (see PR #89)
    if (prev_token == 1 && piece[0] == ' ') { piece++; }
    // careful, some tokens designate raw bytes, and look like e.g. '<0x01>'
    // parse this and convert and return the actual byte
    unsigned char byte_val;
    if (sscanf(piece, "<0x%02hhX>", &byte_val) == 1) {
        piece = (char*)t->byte_pieces + byte_val * 2;
        piece[0] = byte_val;
        piece[1] = '\0';
    }
    return piece;
}

void safe_printf(char* piece) {
    // piece might be a raw byte token, and we only want to print printable chars or whitespace
    // some of the other bytes can be various control codes, backspace, etc.
    if (piece == NULL) { return; }
    if (piece[0] == '\0') { return; }
    if (piece[1] == '\0') {
        unsigned char byte_val = piece[0];
        if (!(isprint(byte_val) || isspace(byte_val))) {
            return; // bad byte, don't print it
        }
    }
    printf("%s", piece);
}

int tokenizer_init(Tokenizer* t, char* tokenizer_path, int vocab_size) {
    // i should have written the vocab_size into the tokenizer file... sigh
    t->vocab_size = vocab_size;
    // malloc space to hold the scores and the strings
    t->vocab = (char**)malloc(vocab_size * sizeof(char*));
    t->vocab_scores = (float*)malloc(vocab_size * sizeof(float));
    t->sorted_vocab = NULL; // initialized lazily
    for (int i = 0; i < 256; i++) {
        t->byte_pieces[i * 2] = (unsigned char)i;
        t->byte_pieces[i * 2 + 1] = '\0';
    }
    // read in the file
    FILE* file = fopen(tokenizer_path, "rb");
    if (!file) {
        fprintf(stderr, "couldn't load %s\n", tokenizer_path);
        return 1;
    }
    if (fread(&t->max_token_length, sizeof(int), 1, file) != 1) {
        fprintf(stderr, "failed read\n");
        return 1;
    }
    int len;
    for (int i = 0; i < vocab_size; i++) {
        if (fread(&t->vocab_scores[i], sizeof(float), 1, file) != 1) {
            fprintf(stderr, "failed read\n");
            return 1;
        }
        if (fread(&len, sizeof(int), 1, file) != 1) {
            fprintf(stderr, "failed read\n");
            return 1;
        }
        t->vocab[i] = (char*)malloc(len + 1);
        if (fread(t->vocab[i], len, 1, file) != 1) {
            fprintf(stderr, "failed read\n");
            return 1;
        }
        t->vocab[i][len] = '\0'; // add the string terminating token
    }
    fclose(file);
    return 0;
}

void tokenizer_free(Tokenizer* t) {
    if (t->vocab) {
        for (int i = 0; i < t->vocab_size; i++) { free(t->vocab[i]); }
        free(t->vocab);
    }
    if (t->vocab_scores) { free(t->vocab_scores); }
    if (t->sorted_vocab) { free(t->sorted_vocab); }
}

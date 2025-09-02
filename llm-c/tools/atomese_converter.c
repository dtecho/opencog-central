
#include "../include/llm_core.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Atomese format converter for OpenCog integration
typedef struct {
    char* atomese_expression;
    char* natural_language;
    float confidence;
} AtomeseMapping;

// Convert natural language to Atomese
char* natural_to_atomese(const char* natural_text) {
    char* atomese = malloc(1024);
    
    // Simple pattern matching for basic conversions
    if (strstr(natural_text, "is a") || strstr(natural_text, "is an")) {
        // "X is a Y" -> (InheritanceLink (ConceptNode "X") (ConceptNode "Y"))
        char subject[128], object[128];
        if (sscanf(natural_text, "%s is a %s", subject, object) == 2 ||
            sscanf(natural_text, "%s is an %s", subject, object) == 2) {
            snprintf(atomese, 1024, 
                "(InheritanceLink\n"
                "  (ConceptNode \"%s\")\n"
                "  (ConceptNode \"%s\"))", subject, object);
        }
    }
    else if (strstr(natural_text, "likes") || strstr(natural_text, "loves")) {
        // "X likes Y" -> (EvaluationLink (PredicateNode "likes") (ListLink (ConceptNode "X") (ConceptNode "Y")))
        char subject[128], object[128];
        if (sscanf(natural_text, "%s likes %s", subject, object) == 2 ||
            sscanf(natural_text, "%s loves %s", subject, object) == 2) {
            snprintf(atomese, 1024,
                "(EvaluationLink\n"
                "  (PredicateNode \"likes\")\n"
                "  (ListLink\n"
                "    (ConceptNode \"%s\")\n"
                "    (ConceptNode \"%s\")))", subject, object);
        }
    }
    else if (strstr(natural_text, "and")) {
        // "X and Y" -> (AndLink (ConceptNode "X") (ConceptNode "Y"))
        char first[128], second[128];
        if (sscanf(natural_text, "%s and %s", first, second) == 2) {
            snprintf(atomese, 1024,
                "(AndLink\n"
                "  (ConceptNode \"%s\")\n"
                "  (ConceptNode \"%s\"))", first, second);
        }
    }
    else {
        // Default: wrap as ConceptNode
        snprintf(atomese, 1024, "(ConceptNode \"%s\")", natural_text);
    }
    
    return atomese;
}

// Convert Atomese back to natural language
char* atomese_to_natural(const char* atomese_expr) {
    char* natural = malloc(512);
    
    if (strstr(atomese_expr, "InheritanceLink")) {
        // Extract concept nodes for "X is a Y" pattern
        // Simplified extraction
        strcpy(natural, "inheritance relationship detected");
    }
    else if (strstr(atomese_expr, "EvaluationLink")) {
        strcpy(natural, "evaluation relationship detected");
    }
    else if (strstr(atomese_expr, "AndLink")) {
        strcpy(natural, "conjunction detected");
    }
    else {
        strcpy(natural, "concept detected");
    }
    
    return natural;
}

// Batch convert text file to Atomese
int convert_file_to_atomese(const char* input_file, const char* output_file) {
    FILE* in = fopen(input_file, "r");
    FILE* out = fopen(output_file, "w");
    
    if (!in || !out) {
        printf("Error opening files\n");
        return -1;
    }
    
    char line[1024];
    int conversions = 0;
    
    fprintf(out, ";; Atomese conversion from %s\n\n", input_file);
    
    while (fgets(line, sizeof(line), in)) {
        // Remove newline
        line[strcspn(line, "\n")] = 0;
        
        if (strlen(line) > 0) {
            char* atomese = natural_to_atomese(line);
            fprintf(out, ";; Original: %s\n%s\n\n", line, atomese);
            free(atomese);
            conversions++;
        }
    }
    
    fclose(in);
    fclose(out);
    
    printf("Converted %d expressions to Atomese format\n", conversions);
    return conversions;
}

// Command-line interface
int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <command> [args]\n", argv[0]);
        printf("Commands:\n");
        printf("  convert <input_file> <output_file> - Convert text to Atomese\n");
        printf("  expr <text> - Convert single expression\n");
        return 1;
    }
    
    if (strcmp(argv[1], "convert") == 0 && argc >= 4) {
        return convert_file_to_atomese(argv[2], argv[3]);
    }
    else if (strcmp(argv[1], "expr") == 0 && argc >= 3) {
        char* atomese = natural_to_atomese(argv[2]);
        printf("Natural: %s\n", argv[2]);
        printf("Atomese: %s\n", atomese);
        free(atomese);
        return 0;
    }
    
    printf("Invalid command or arguments\n");
    return 1;
}

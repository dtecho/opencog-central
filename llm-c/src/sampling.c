
#include "llm_core.h"
#include <time.h>
#include <string.h>

int sample_argmax(float* probabilities, int n) {
    // Return the index that has the highest probability
    int max_i = 0;
    float max_p = probabilities[0];
    for (int i = 1; i < n; i++) {
        if (probabilities[i] > max_p) {
            max_i = i;
            max_p = probabilities[i];
        }
    }
    return max_i;
}

int sample_mult(float* probabilities, int n, float coin) {
    // Sample index from probabilities (they must sum to 1!)
    // coin is a random number in [0, 1), usually from random_f32()
    float cdf = 0.0f;
    for (int i = 0; i < n; i++) {
        cdf += probabilities[i];
        if (coin < cdf) {
            return i;
        }
    }
    return n - 1; // in case of rounding errors
}

int compare(const void* a, const void* b) {
    float fa = *(const float*)a;
    float fb = *(const float*)b;
    return (fa > fb) - (fa < fb);
}

int sample_topp(float* probabilities, int n, float topp, float* probabilities_sorted, int* indices) {
    // top-p sampling (or "nucleus sampling") samples from the smallest set of
    // tokens that exceed probability topp. This way we never sample tokens that
    // have very low probabilities and are less likely to go "off the rails".

    int n_sorted = 0;
    for (int i = 0; i < n; i++) {
        probabilities_sorted[n_sorted] = probabilities[i];
        indices[n_sorted] = i;
        n_sorted++;
    }

    // Sort indices in descending order of probabilities
    // values smaller -> indices smaller
    for (int i = 0; i < n_sorted - 1; i++) {
        for (int j = i + 1; j < n_sorted; j++) {
            if (probabilities_sorted[i] < probabilities_sorted[j]) {
                // Swap probabilities
                float temp = probabilities_sorted[i];
                probabilities_sorted[i] = probabilities_sorted[j];
                probabilities_sorted[j] = temp;
                // Swap indices
                int temp_idx = indices[i];
                indices[i] = indices[j];
                indices[j] = temp_idx;
            }
        }
    }

    // Truncate the list where cumulative probability exceeds topp
    float cumulative_prob = 0.0f;
    int last_idx = n_sorted - 1; // in case of rounding errors consider all elements
    for (int i = 0; i < n_sorted; i++) {
        cumulative_prob += probabilities_sorted[i];
        if (cumulative_prob > topp) {
            last_idx = i;
            break; // we've exceeded topp by including last_idx
        }
    }

    // Sample from the truncated list
    float r = ((float)rand() / (float)RAND_MAX) * cumulative_prob;
    float cdf = 0.0f;
    for (int i = 0; i <= last_idx; i++) {
        cdf += probabilities_sorted[i];
        if (r < cdf) {
            return indices[i];
        }
    }
    return indices[last_idx]; // in case of rounding errors
}


#include <math.h>
#include <string.h>
#include "../include/llm_core.h"

typedef struct {
    float* m;  // First moment estimates
    float* v;  // Second moment estimates
    int step;  // Time step
    float beta1;
    float beta2;
    float eps;
    float lr;
} adam_optimizer_t;

adam_optimizer_t* create_adam_optimizer(int param_count, float lr, 
                                       float beta1, float beta2, float eps) {
    adam_optimizer_t* opt = malloc(sizeof(adam_optimizer_t));
    if (!opt) return NULL;
    
    opt->m = calloc(param_count, sizeof(float));
    opt->v = calloc(param_count, sizeof(float));
    
    if (!opt->m || !opt->v) {
        free(opt->m);
        free(opt->v);
        free(opt);
        return NULL;
    }
    
    opt->step = 0;
    opt->beta1 = beta1;
    opt->beta2 = beta2;
    opt->eps = eps;
    opt->lr = lr;
    
    return opt;
}

void adam_step(adam_optimizer_t* opt, float* params, const float* gradients, 
               int param_count) {
    opt->step++;
    
    float beta1_t = powf(opt->beta1, opt->step);
    float beta2_t = powf(opt->beta2, opt->step);
    float lr_t = opt->lr * sqrtf(1.0f - beta2_t) / (1.0f - beta1_t);
    
    for (int i = 0; i < param_count; i++) {
        // Update biased first moment estimate
        opt->m[i] = opt->beta1 * opt->m[i] + (1.0f - opt->beta1) * gradients[i];
        
        // Update biased second moment estimate
        opt->v[i] = opt->beta2 * opt->v[i] + (1.0f - opt->beta2) * gradients[i] * gradients[i];
        
        // Update parameters
        params[i] -= lr_t * opt->m[i] / (sqrtf(opt->v[i]) + opt->eps);
    }
}

void destroy_adam_optimizer(adam_optimizer_t* opt) {
    if (opt) {
        free(opt->m);
        free(opt->v);
        free(opt);
    }
}

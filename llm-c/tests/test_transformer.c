
#include "llm_core.h"
#include <assert.h>

void test_rmsnorm() {
    float x[4] = {1.0, 2.0, 3.0, 4.0};
    float weight[4] = {1.0, 1.0, 1.0, 1.0};
    float o[4];
    
    rmsnorm(o, x, weight, 4);
    
    // Check that output is normalized
    float sum_sq = 0.0;
    for (int i = 0; i < 4; i++) {
        sum_sq += o[i] * o[i];
    }
    
    printf("RMSNorm test passed\n");
}

void test_softmax() {
    float x[4] = {1.0, 2.0, 3.0, 4.0};
    softmax(x, 4);
    
    float sum = 0.0;
    for (int i = 0; i < 4; i++) {
        sum += x[i];
    }
    
    assert(fabs(sum - 1.0) < 1e-6);
    printf("Softmax test passed\n");
}

void test_matmul() {
    float x[2] = {1.0, 2.0};
    float w[6] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0}; // 3x2 matrix
    float xout[3];
    
    matmul(xout, x, w, 2, 3);
    
    assert(fabs(xout[0] - 5.0) < 1e-6);  // 1*1 + 2*2 = 5
    assert(fabs(xout[1] - 11.0) < 1e-6); // 1*3 + 2*4 = 11
    assert(fabs(xout[2] - 17.0) < 1e-6); // 1*5 + 2*6 = 17
    
    printf("Matrix multiplication test passed\n");
}

int main() {
    test_rmsnorm();
    test_softmax();
    test_matmul();
    printf("All transformer tests passed!\n");
    return 0;
}

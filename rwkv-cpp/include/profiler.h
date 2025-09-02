
#pragma once

#include <chrono>
#include <string>
#include <unordered_map>
#include <vector>

namespace rwkv_cpp {

struct ProfileData {
    double total_time_ms;
    double avg_time_ms;
    double min_time_ms;
    double max_time_ms;
    size_t call_count;
};

class Profiler {
public:
    static Profiler& instance();
    
    void start_timer(const std::string& name);
    void end_timer(const std::string& name);
    
    ProfileData get_profile(const std::string& name) const;
    std::vector<std::string> get_all_profiles() const;
    
    void reset();
    void print_summary() const;

private:
    Profiler() = default;
    
    std::unordered_map<std::string, std::chrono::high_resolution_clock::time_point> active_timers_;
    std::unordered_map<std::string, std::vector<double>> measurements_;
};

// RAII timer helper
class ScopedTimer {
public:
    explicit ScopedTimer(const std::string& name) : name_(name) {
        Profiler::instance().start_timer(name_);
    }
    
    ~ScopedTimer() {
        Profiler::instance().end_timer(name_);
    }

private:
    std::string name_;
};

#define RWKV_PROFILE(name) rwkv_cpp::ScopedTimer _timer(name)

} // namespace rwkv_cpp

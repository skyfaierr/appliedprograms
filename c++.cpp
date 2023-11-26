#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

// Функция для вычисления среднего арифметического
double calculateMean(const std::vector<double>& numbers) {
    if (numbers.empty()) { return 0.0; }
    double sum = std::accumulate(numbers.begin(), numbers.end(), 0.0);
    return sum / numbers.size();
}

// Функция для нахождения наибольшего значения
double findMax(const std::vector<double>& numbers) {
    if (numbers.empty()) { return 0.0; }
    return *std::max_element(numbers.begin(), numbers.end());
}

// Функция для нахождения наименьшего значения
double findMin(const std::vector<double>& numbers) {
    if (numbers.empty()) { return 0.0; }
    return *std::min_element(numbers.begin(), numbers.end());
}

// Функция для вычисления суммы всех значений
double calculateSum(const std::vector<double>& numbers) {
    return std::accumulate(numbers.begin(), numbers.end(), 0.0);
}

int main() {
    std::vector<double> numbers = {1.5, 2.0, 3.7, 2.5, 4.8, 1.0};

    std::cout << "Среднее арифметическое: " << calculateMean(numbers) << std::endl;
    std::cout << "Наибольшее значение: " << findMax(numbers) << std::endl;
    std::cout << "Наименьшее значение: " << findMin(numbers) << std::endl;
    std::cout << "Сумма всех значений: " << calculateSum(numbers) << std::endl;

    return 0;
}

#include <iostream>

#include "models/Transaction.h"
#include "managers/TransactionManager.h"
#include "filters/FilterEngine.h"
#include "reports/ReportGenerator.h"

int main()
{
    TransactionManager manager;

    manager.addTransaction(
        3000,
        Category::Salary,
        TransactionType::Income,
        "Monthly Salary");

    manager.addTransaction(
        50,
        Category::Food,
        TransactionType::Expense,
        "Dinner");

    manager.addTransaction(
        1000,
        Category::Rent,
        TransactionType::Expense,
        "Apartment rent");

    manager.addTransaction(
        200,
        Category::Investment,
        TransactionType::Income,
        "Stock dividend");

    auto transactions = manager.getAll();

    double income = ReportGenerator::totalIncome(transactions);
    double expense = ReportGenerator::totalExpense(transactions);
    double balance = ReportGenerator::balance(transactions);

    std::cout << "===== Financial Summary =====" << std::endl;

    std::cout << "Total Income: " << income << std::endl;
    std::cout << "Total Expense: " << expense << std::endl;
    std::cout << "Balance: " << balance << std::endl;

    auto foodExpenses = FilterEngine::filter(
        transactions,
        [](const auto& t)
        {
            return t->getCategory() == Category::Food &&
                   t->getType() == TransactionType::Expense;
        });

    std::cout << "\nFood Expenses Count: "
              << foodExpenses.size()
              << std::endl;

    return 0;
}
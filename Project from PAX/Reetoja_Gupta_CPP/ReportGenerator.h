#ifndef REPORT_GENERATOR_H
#define REPORT_GENERATOR_H

#include <vector>
#include <memory>

#include "../models/Transaction.h"
#include "../utils/Aggregator.h"

class ReportGenerator
{
public:

    static double totalIncome(
        const std::vector<std::shared_ptr<Transaction>>& data)
    {
        return aggregate(data.begin(), data.end(),
            [](const auto& t)
            {
                return (t->getType() == TransactionType::Income)
                        ? t->getAmount() : 0.0;
            });
    }

    static double totalExpense(
        const std::vector<std::shared_ptr<Transaction>>& data)
    {
        return aggregate(data.begin(), data.end(),
            [](const auto& t)
            {
                return (t->getType() == TransactionType::Expense)
                        ? t->getAmount() : 0.0;
            });
    }

    static double balance(
        const std::vector<std::shared_ptr<Transaction>>& data)
    {
        return totalIncome(data) - totalExpense(data);
    }
};

#endif
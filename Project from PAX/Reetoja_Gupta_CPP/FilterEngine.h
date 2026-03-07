#ifndef FILTER_ENGINE_H
#define FILTER_ENGINE_H

#include <vector>
#include <memory>
#include <algorithm>
#include <functional>

#include "../models/Transaction.h"

class FilterEngine
{
public:

    static std::vector<std::shared_ptr<Transaction>>
    filter(const std::vector<std::shared_ptr<Transaction>>& data,
           std::function<bool(const std::shared_ptr<Transaction>&)> predicate)
    {
        std::vector<std::shared_ptr<Transaction>> result;

        std::copy_if(
            data.begin(),
            data.end(),
            std::back_inserter(result),
            predicate
        );

        return result;
    }
};

#endif
#ifndef AGGREGATOR_H
#define AGGREGATOR_H

template<typename Iterator, typename Func>
double aggregate(Iterator begin, Iterator end, Func accessor)
{
    double total = 0;

    for (auto it = begin; it != end; ++it)
    {
        total += accessor(*it);
    }

    return total;
}

#endif
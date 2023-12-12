#include "Source.h"
#include "RandomNumberGenerator.h"
#include "Sampling.h"

#include <iostream>
#include <numeric>

    Source::Source(InputParameters & parameters) :
                    _positions(parameters.sourcePositions()),
                    _angular_distribution(parameters.sourceAngularDistribution()),
                    _direction_cosines(parameters.sourceDirectionCosines())
    {
        int source_size = _positions.size();
        _normalized_probability.resize(source_size);
        _cumulative_probability.resize(source_size);
        std::vector<double> unnormalized_probability = parameters.sourceProbability();
        double unnormalized_sum = std::accumulate(unnormalized_probability.begin(), unnormalized_probability.end(), 0);
        double cumulative_sum = 0;

        for (int i = 0; i < source_size; ++i)
        {
            _normalized_probability[i] = unnormalized_probability[i] / unnormalized_sum;
            cumulative_sum += _normalized_probability[i];
            _cumulative_probability[i] = cumulative_sum;
        }
    }

    std::vector<std::array<double, 3>> Source::positions()
    { return _positions; }

    std::vector<double> Source::normalizedProbability()
    { return _normalized_probability; }

    std::vector<double> Source::cumulativeProbability()
    { return _cumulative_probability; }

    std::vector<char> Source::angularDistribution()
    { return _angular_distribution; }

    std::vector<std::array<double, 3>> Source::directionCosines()
    { return _direction_cosines; }

    int Source::samplePositionIndex()
    {
        double random_number = randomNumber();
        int source_index;
        int source_size = _positions.size();
        for (int i = 0; i < source_size; ++i)
        {
            if(random_number <= _cumulative_probability[i])
            {
                source_index = i;
                break;
            }
        }
        return source_index;
    }

    std::array<double, N_DIMS> Source::sampledPosition(int source_index)
    { return _positions[source_index]; }

    std::array<double, N_DIMS> Source::sampledDirection(int source_index)
    {
        if (_angular_distribution[source_index] == 'm')
            return _direction_cosines[source_index];
        else
        {
            std::array<double, N_DIMS> mu;
            for (int i = 0; i < N_DIMS; ++i)
                mu[i] = sampling::mu();
            return mu;
        }
    }
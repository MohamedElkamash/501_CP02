#pragma once

#include "Global.h"
#include "InputParameters.h"

#include <vector>
#include <array>

class Source
{
    public:

    Source(InputParameters & parameters);

    std::vector<std::array<double, N_DIMS>> positions();

    std::vector<double> normalizedProbability();

    std::vector<double> cumulativeProbability();

    std::vector<char> angularDistribution();

    std::vector<std::array<double, 3>> directionCosines();

    //returns the index of the sampled source position
    int samplePositionIndex();

    std::array<double, N_DIMS> sampledPosition(int source_index);

    std::array<double, N_DIMS> sampledDirection(int source_index);

    private:

    std::vector<std::array<double, N_DIMS>> _positions;

    std::vector<double> _normalized_probability;

    std::vector<double> _cumulative_probability;

    std::vector<char> _angular_distribution;

    std::vector<std::array<double, N_DIMS>> _direction_cosines;
};
#pragma once

#include "Global.h"

#include <string>
#include <array>
#include <vector>
#include <map>

/*This class carries all the input parameters*/

class InputParameters
{
    typedef std::array<int, N_DIMS> Id_3d;

    public:
    
    //constructor, will be updated in the future to read data from input file
    InputParameters();

    //number of cells 
    std::vector<int> cellCount();

    //minimum point coordinates in the mesh
    std::vector<double> rMin();

    //maximum point coordinates in the mesh
    std::vector<double> rMax();

    //number of materials in the problem
    int materialsCount();

    //carries cross_sections of each material
    std::vector<std::map<int, double>> crossSections();

    //maps each cell with its material
    //each cell has one material only but each material can have many cells
    std::map<Id_3d, int> cellMaterialMap();

    std::vector<std::array<double, 3>> sourcePositions();

    std::vector<double> sourceProbability();

    std::vector<char> sourceAngularDistribution();

    std::vector<std::array<double, 3>> sourceDirectionCosines();

    private:

    //number of cells 
    std::vector<int> _cell_count;

    //minimum point coordinates in the mesh
    std::vector<double> _r_min;

    //maximum point coordinates in the mesh
    std::vector<double> _r_max;

    //number of materials in the problem
    int _materials_count;

    //carries cross_sections of each material
    std::vector<std::map<int, double>> _cross_sections;

    //maps each cell with its material
    //each cell has one material only but each material can have many cells
    std::map<Id_3d, int> _cell_material_map;

    //source information
    std::vector<std::array<double, 3>> _source_positions;

    std::vector<double> _source_probability;

    std::vector<char> _source_angular_distribution;

    std::vector<std::array<double, N_DIMS>> _source_direction_cosines;
};
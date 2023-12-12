#include "Geometry.h"
#include "Global.h"

#include <array>
#include<vector>
#include<iostream>

typedef std::array<int, 3> Id_3d;
typedef std::map<std::array<int, 3>, Cell> Mesh;

//Member Attributes

Geometry::Geometry(InputParameters & parameters) :
_cell_count(parameters.cellCount()),
_r_min(parameters.rMin()),
_r_max(parameters.rMax())
{
    //materials construction
    int materials_count = parameters.materialsCount();
    for (int material_id = 0; material_id < materials_count; ++material_id)
    {
        Material material(material_id, parameters.crossSections()[material_id]);
        _materials.push_back(material);
    }

    //getting cell_width
    for (int i = 0; i < N_DIMS; ++i)
        _cell_width.push_back((_r_max[i] - _r_min[i]) / _cell_count[i]);
    
    //surfaces construction
    for (int dim = 0; dim < N_DIMS; ++dim)
    {
        std::vector<Surface> surfaces;
        int surface_id = 0;
        double r = _r_min[dim];
        while (r <= _r_max[dim])
        {
            Surface surface(surface_id, dim, r);
            surfaces.push_back(surface);
            ++surface_id;
            r += _cell_width[dim];
        }
        _surfaces[dim] = surfaces;
    }
    
    //cell construction
    for (int i=0; i < _cell_count[0]; ++i)
    {
        for (int j=0; j < _cell_count[1]; ++j)
        {
            for (int k=0; k < _cell_count[2]; ++k)
            {
                Id_3d cell_id = {i,j,k};
                int material_id = parameters.cellMaterialMap()[cell_id];
                Material material_in_cell = _materials[material_id];
                std::vector<Surface> bounding_surfaces;
                bounding_surfaces.push_back(_surfaces[0][i]);
                bounding_surfaces.push_back(_surfaces[0][i+1]);
                bounding_surfaces.push_back(_surfaces[1][j]);
                bounding_surfaces.push_back(_surfaces[1][j+1]);
                bounding_surfaces.push_back(_surfaces[2][k]); 
                bounding_surfaces.push_back(_surfaces[2][k+1]);
                Cell cell(cell_id, bounding_surfaces, material_in_cell);
                _cells.insert({cell_id, cell});    
            }
        }
    }


    
}

std::vector<int> Geometry::cellCount()
{ return _cell_count; }

std::vector<double> Geometry::rMin()
{ return _r_min; }

std::vector<double> Geometry::rMax()
{ return _r_max; }

std::vector<double> Geometry::cellWidth()
{ return _cell_width; }

std::map<int, std::vector<Surface>> Geometry::surfaces()
{ return _surfaces; }

std::vector<Material> Geometry::materials()
{ return _materials; }

Mesh Geometry::cells()
{ return _cells; }

/* 






int Geometry::cellCount()
{ return _cells.size(); }

double Geometry::xMin()
{ return _cells[0].xLeft(); }

double Geometry::xMax()
{ return _cells[cellCount() - 1].xRight(); }

double Geometry::GeometryWidth()
{ return xMax() - xMin(); }

double Geometry::cellWidth(int id)
{ return _cells[id].cellWidth(); } 

int Geometry::materialCount()
{ return _materials.size(); }

std::vector<double> Geometry::binsWidthVector()
{
    std::vector<double> bins_width;
    int bins = cellCount();
    for (int i = 0; i < bins; ++i)
        bins_width.push_back(cellWidth(i));
    
    return bins_width;
    }
*/

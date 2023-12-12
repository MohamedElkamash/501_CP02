#include "Cell.h"

typedef std::array<int, 3> Id_3d;

Cell::Cell(Id_3d id, std::vector<Surface> surfaces, const Material & material) :
_id(id),
_surfaces(surfaces),
_material(material)
{}

/* Cell::Cell(Cell & cell) : _material(cell._material),  _id(cell._id), _surfaces(cell._surfaces)
{
   
} */

Id_3d Cell::id()
{ return _id; }

std::vector<Surface> Cell::surfaces()
{ return _surfaces; }

Material Cell::material()
{ return _material; } 




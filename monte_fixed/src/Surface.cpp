#include "Surface.h"

Surface::Surface(int id, int axis, double coordinate) :
_id(id),
_axis(axis),
_coordinate(coordinate)
{}

int Surface::id()
{ return _id; }

int Surface::axis()
{ return _axis; }

double Surface::coordinate()
{ return _coordinate; }

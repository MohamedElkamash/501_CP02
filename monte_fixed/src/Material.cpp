#include "Material.h"

#include <string>
#include <map>

Material::Material(int id, std::map<int, double> cross_sections):
_id(id),
_cross_sections(cross_sections)
{ _cross_sections[2] = _cross_sections[0] + _cross_sections[1]; }

int Material::id()
{ return _id; }

std::map<int, double> Material::crossSections()
{ return _cross_sections; }

double Material::totalXS()
{ return _cross_sections[2]; }

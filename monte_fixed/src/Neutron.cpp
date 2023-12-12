#include "Neutron.h"

Neutron::Neutron(int id, std::array<double, 3> position, std::array<double, 3> mu):
_id(id),
_position(position),
_mu(mu)
{}

int Neutron::id()
{ return _id; }

std::array<double, 3> Neutron::position()
{ return _position; }

std::array<double, 3> Neutron::mu()
{ return _mu; }

void Neutron::updatePosition(std::array<double, 3> position)
{ _position = position; }

void Neutron::updateMu(std::array<double, 3> mu)
{ _mu = mu; }

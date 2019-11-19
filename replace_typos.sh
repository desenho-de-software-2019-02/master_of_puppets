#!/bin/bash
find . -regex ".*\.\(py\|ts\|html\)" | xargs sed -i 's/desterity/dexterity/g; s/inteligence/intelligence/g; s/klass/character_class/g; s/klasses/character_classes/g; s/attack_bonus/bonus_attack/g; s/costitution/constitution/g;'

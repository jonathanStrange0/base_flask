#!/bin/bash

source venv bin activate
flask db upgrade

flask db init

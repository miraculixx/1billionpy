#!/bin/bash

# Function to add a program to the global array
add() {
  if [[ -f ${3} ]]; then
    input=$(cat input.txt)
    names+=("$1")
    programs+=("$2 $3 $input")
  fi
}

# Function to run hyperfine for all programs in the global array
run() {
  for name in "${names[@]}"; do
    hyperfine_name_args+=("-n '$name'")
  done
  for program in "${programs[@]}"; do
    hyperfine_program_args+=("'$program'")
  done
  cmd="hyperfine -i --shell=sh -C 'sleep 5' --runs 3 --warmup 2 --export-json reports.json ${hyperfine_name_args[@]} ${hyperfine_program_args[@]}"
  echo "[INFO] running $cmd"
  eval $cmd
}

plot() {
  echo "[INFO] plotting..."
  pip install matplotlib
  python create_plot.py reports.json
}

# install
echo "[INFO] install"
python3.10 -m pip install -U --user numba numpy scipy
if [[ ! -f ./pypy ]]; then
  wget https://downloads.python.org/pypy/pypy3.10-v7.3.17-linux64.tar.bz2
  tar -xf pypy3.10-v7.3.17-linux64.tar.bz2
  ln -fs "$(find . -name pypy)" ./pypy
fi

# compile
echo "[INFO] compiling"
clang -O3 baseline.c -o baseline; chmod +x ./baseline
CFLAGS=-O3 cythonize -3 -f -i ap7.py
python -m compileall -o3 -f $(ls *.py)
export PYTHON_JIT=0

echo "[INFO] building benchmark suite"
add "C (baseline)" "" "./baseline"
# -- python
add "Python (baseline)" "python" "baseline.py"
add "Python (cython)" "python" "ap7.py"
add "Python (vec)" "python" "ap14.py"
add "Python (vec.np)" "python" "ap15.py"
add "Python (numba)" "python3.10" "ap10.py"
add "Python (numba.np)" "python3.10" "ap11.py"
add "Python (numba.np.vec)" "python3.10" "ap20.py"
add "Python (parallel)" "python" "ap17.py"
add "Python (parallel.np)" "python" "ap18.py"
add "Python (np)" "python" "ap19.py"
# -- pypy
add "Pypy (baseline)" "./pypy" "baseline.py"
add "Pypy (vec)" "./pypy" "ap14.py"
add "Pypy (vec.np)" "./pypy" "ap15.py"
add "Pypy (parallel)" "./pypy" "ap17.py"
add "Pypy (parallel.np)" "./pypy" "ap18.py"

# run and plot
run
plot
echo "[INFO] done"
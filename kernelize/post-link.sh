#!/usr/bin/env bash

# Create a kernel for this env

ENV_NAME=$(basename ${PREFIX})

echo "Creating kernel for the \"${ENV_NAME}\" env." > $PREFIX/.messages.txt

mkdir -p $PREFIX/share/jupyter/kernels/env_${ENV_NAME}
cat > $PREFIX/share/jupyter/kernels/env_${ENV_NAME}/kernel.json <<EOF
{
 "display_name": "ENV: ${ENV_NAME}",
 "language": "python",
 "codemirror_mode": {
  "version": 3,
  "name": "ipython"
 },
 "argv": [
  "${PREFIX}/bin/python",
  "-c",
  "from IPython.kernel.zmq.kernelapp import main; main()",
  "-f",
  "{connection_file}"
 ]
}
EOF

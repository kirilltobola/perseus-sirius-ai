# Установка библиотек `llama_cpp` и `langchain`

## Windows
Должны быть установлены:
- git
- python
- cmake
- Visual Studio Community (make sure you install this with the following settings)
-- Desktop development with C++
-- Python development
-- Linux embedded development with C++

1. `git clone --recursive -j8 https://github.com/abetlen/llama-cpp-python.git`
2. `set FORCE_CMAKE=1`
3. `set CMAKE_ARGS=-DLLAMA_CUBLAS=OFF` # CPU-only `set CMAKE_ARGS=-DLLAMA_CUBLAS=OFF` # GPU support
4. `python -m pip install -e .`

## Linux
Должны быть установлены:
- gcc
- make
- cmake

### CPU
`pip install --upgrade --quiet  llama-cpp-python`

### GPU
`CMAKE_ARGS="-DLGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python`

# Где искать скомпилированные LLM?

- https://huggingface.co/
- можно скачать в LM studio и найти файл в папке загрузок

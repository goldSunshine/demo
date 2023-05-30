
# 表修改
python db/run_migrate.py run_migrate

# python 环境变量
export PYTHONPATH = $PYTHONPATH:$(dirname $(pwd))

# 启动flask
python main.py

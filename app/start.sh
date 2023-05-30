
# python 环境变量
export PYTHONPATH=$PYTHONPATH:$(dirname $(pwd))


# 表更新
python db/run_migrate.py run_migrate


# 启动flask
python main.py



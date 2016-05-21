# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError

from app import app

import xxxiao


engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


@engine.define
def fetchImageFromXxxiao(**params):
	print xxxiao.fetchImageSeriesByPageNum(1)
	return 'OK'


@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')

import json

from antlr4 import *

from .fuzzy import defuzzifiers
from .fuzzy import functions
from .fuzzy import models
from .fuzzy.parsing.FuzzyLexer import FuzzyLexer
from .fuzzy.parsing.FuzzyParser import FuzzyParser
from .fuzzy.parsing.evaluator import Evaluator


def print_dict(d: dict):
    for key, value in d.items():
        print('%s: %.3f' % (key, value))


def process(rules_path, args_path):
    # Grab rules, data and step from parsed arguments
    rules = FileStream(rules_path)
    data = json.load(open(args_path))
    step = 0.1

    # Parse rules file
    lexer = FuzzyLexer(rules)
    stream = CommonTokenStream(lexer)
    parser = FuzzyParser(stream)
    tree = parser.compileUnit()

    # Retrieve dictionaries from data JSON file
    values = data['variables']
    funcs = data['functions']

    for f, l in funcs.items():
        f_name = l.pop(0)
        funcs[f] = getattr(functions, f_name)(*l)

    # Evaluate rules expressions
    evaluator = Evaluator(values, funcs)
    model, defuzzy, output = evaluator.visit(tree)

    model = model.lower()

    if model == 'mamdani':
        defuzzy = getattr(defuzzifiers, defuzzy.lower())
        return models.mamdani(output, defuzzy, funcs, step)

    elif model == 'sugeno':
        return models.sugeno(output)

    elif model == 'tsukamoto':
        return models.tsukamoto(output, funcs, step)

    else:
        raise AttributeError()
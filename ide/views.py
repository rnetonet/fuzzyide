from django.shortcuts import render
from .models import System
import tempfile
import json

from fuzzy_evaluator import fuzzy_evaluator

# Create your views here.
def index(request):
    return render(request, "ide/index.html", locals())

def process_system(request, pk):
    system = System.objects.get(pk=pk)
    
    rules = tempfile.NamedTemporaryFile(mode="w", delete=False)
    args = tempfile.NamedTemporaryFile(mode="w", delete=False)

    # Writing rules
    print(rules.name)
    print(args.name)

    # rules
    rules.write(f"[model] {system.fuzzy_model.name.capitalize()}\n")
    rules.write("\n")
    rules.write(f"[t-norm] {system.tnorm.name.lower()}\n")
    rules.write(f"[t-conorm] {system.conorm.name.lower()}\n")
    rules.write(f"[defuzzy] {system.defuzzy.name.lower()}\n")
    rules.write("\n")
    for rule in system.rule_set.all():
        rules.write(rule.rule + "\n")
    rules.close()

    j = {}
    
    j["variables"] = {}
    for variable in system.variable_set.all():
        j["variables"][variable.name] = variable.value
    
    j["functions"] = {}
    for function in system.function_set.all():
        
        lst = [function.category.name.capitalize()]

        if not function.a is None:
            lst.append(function.a)
        else:
            lst.append("null")

        if function.b: lst.append(function.b)
        if function.c: lst.append(function.c)
        if function.d: lst.append(function.d)
        
        j["functions"][function.name] = lst

    j = json.dumps(j, indent=4).replace('"null"', "null")

    args.write(j)
    args.close()

    result = fuzzy_evaluator.process(rules.name, args.name)

    return render(request, "ide/index.html", locals())
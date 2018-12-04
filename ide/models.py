from django.db import models
import tempfile

# Create your models here.
class FuzzyModel(models.Model):
    name = models.CharField("t-norm", max_length=256)

    class Meta:
        verbose_name = "Fuzzy Model"

    def __str__(self):
        return f"model: {self.name}"


class TNorm(models.Model):
    name = models.CharField("t-norm", max_length=256)

    class Meta:
        verbose_name = "T-Norm"

    def __str__(self):
        return f"t-norm: {self.name}"


class CONorm(models.Model):
    name = models.CharField("co-norm", max_length=256)

    class Meta:
        verbose_name = "Co-Norm"

    def __str__(self):
        return f"co-norm: {self.name}"


class DeFuzzy(models.Model):
    name = models.CharField("co-norm", max_length=256)

    class Meta:
        verbose_name = "DeFuzzy"

    def __str__(self):
        return f"defuzzy: {self.name}"


class System(models.Model):
    fuzzy_model = models.ForeignKey("FuzzyModel", on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=256)
    tnorm = models.ForeignKey("TNorm", on_delete=models.CASCADE)
    conorm = models.ForeignKey("CONorm", on_delete=models.CASCADE)
    defuzzy = models.ForeignKey("DeFuzzy", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.fuzzy_model} | {self.tnorm} | {self.conorm} | {self.defuzzy}"

class Variable(models.Model):
    system = models.ForeignKey("System", on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=256)
    value = models.FloatField("Value")

    def __str__(self):
        return f"{self.system} - {self.name}={self.value}"


class FunctionCategory(models.Model):
    name = models.CharField("Name", max_length=255)
    params = models.CharField("Params", max_length=1024)

    def __str__(self):
        return f"{self.name} - ({self.params})"


class Function(models.Model):
    system = models.ForeignKey("System", on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=256)
    category = models.ForeignKey("FunctionCategory", on_delete=models.CASCADE)
    a = models.FloatField("a", null=True, blank=True)
    b = models.FloatField("b", null=True, blank=True)
    c = models.FloatField("c", null=True, blank=True)
    d = models.FloatField("d", null=True, blank=True)

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return f"{self.system} - {self.name} : {self.category} - ({self.a}, {self.b}, {self.c}, {self.d})"


class Rule(models.Model):
    system = models.ForeignKey("System", on_delete=models.CASCADE)
    rule = models.CharField("Rule", max_length=1024)

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return f"{self.system.name}: {self.rule}"

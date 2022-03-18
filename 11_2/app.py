from flask import Flask, render_template
from utils import load_candidates

data = load_candidates("candidates.json")

print(data)

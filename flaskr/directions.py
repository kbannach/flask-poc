from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('directions', __name__)
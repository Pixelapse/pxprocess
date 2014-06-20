# -*- coding: utf-8 -*-

# Default libs
import os
import sys
import shlex
import subprocess
import logging

from itertools import islice

# Installed libs

# Project modules

logger = logging.getLogger(__name__)


def _isplit(source, sep):
  sepsize = len(sep)
  start = 0
  while True:
    idx = source.find(sep, start)
    if idx == -1:
      yield source[start:]
      return
    yield source[start:idx]
    start = idx + sepsize


def check_call(*args, **kwargs):
  n = kwargs.pop('n', 30)
  proc = subprocess.Popen(*args, stderr=subprocess.PIPE, **kwargs)

  errhead = "\n".join(islice(proc.stderr, n))
  if errhead:
    print >> sys.stderr, errhead

  proc.stderr.close()
  proc.wait()

  if proc.returncode:
    cmd = kwargs.get("args")
    if cmd is None:
      cmd = args[0]
    raise subprocess.CalledProcessError(proc.returncode, cmd)

  return 0


def check_output(*args, **kwargs):
  n = kwargs.pop('n', 30)
  proc = subprocess.Popen(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
  output, err = proc.communicate()

  errhead = "\n".join(islice(_isplit(err, "\n"), n))
  if errhead:
    print >> sys.stderr, errhead

  if proc.returncode:
    cmd = kwargs.get("args")
    if cmd is None:
      cmd = args[0]
    raise subprocess.CalledProcessError(proc.returncode, cmd)

  return output


def call_command(command, shell=False):
  if sys.hexversion < 0x02070300:
    retcode = os.system(command)
    if retcode != 0:
      raise subprocess.CalledProcessError(retcode, command)
    return

  if shell:
    check_call(command, shell=True)
  else:
    check_call(shlex.split(command))


def call_output(command, shell=False):
  if sys.hexversion < 0x02070300:
    return os.popen(command).read()

  if shell:
    return check_output(command, shell=True)
  else:
    return check_output(shlex.split(command))

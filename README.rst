=============
Description
=============

A collection of scripts and notebooks aimed at analysing Uchuu data

Running a jupyter notebook remotely
------------------------------------

Here are the simple steps to analyse data residing on a remote server using jupyter notebook:

1. Login to the remote server and open a ``screen/tmux`` session
2. Start jupyter notebook with ``jupyter-notebook --no-browser`` and note the **token** (you will need this in step 4)
3. From a separate terminal, run this command ``ssh -N -f -L localhost:8889:localhost:8888 <username@remote.server.name>``. You will need to enter your password on the remote server, but you will not get a remote shell; the command maps the remote port (by default ``8888``) to a local port (``8889`` is used here). 
4. Once this session is established, open the page: ``http://localhost:8889/`` in a web browser, and paste in the token from step 2
5. You should now have a working jupyter notebook, where the calculations are performed on the remote server

(Following the instructions from `here <https://ljvmiranda921.github.io/notebook/2018/01/31/running-a-jupyter-notebook/>`_)

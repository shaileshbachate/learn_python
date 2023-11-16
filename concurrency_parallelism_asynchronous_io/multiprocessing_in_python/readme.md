## Reason for not using jupyter notebook for multiprocessing practice:

Jupyter notebooks handle output differently than a standard Python script, especially when it comes to multiprocessing. When you create a new process, Jupyter notebooks may not display the standard output (print statements) of that process in the cell's output area. This is because each process has its own standard output.

In a standard Python script, all output goes to the terminal, so you would see the print statements from each process. But in a Jupyter notebook, the notebook server is the "terminal" and it captures standard output from the main process and directs it to the cell output. It doesn't do this for other processes, which is why you don't see their print statements.

If you want to see the output of each process in your Jupyter notebook, you could write the output to a file, or use a different method of inter-process communication, such as a Queue or Pipe, which are provided by the `multiprocessing` module. However, these methods are more complex and may not be necessary depending on what you're trying to achieve.

For learning and experimenting with multiprocessing, I would recommend running your code as a Python script in a terminal to see the expected output. For more complex applications where you need to capture output from subprocesses, consider using the logging module or a third-party library that's designed for that purpose.

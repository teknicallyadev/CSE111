In this lab session you will learn how to work with \texttt{SQL} views. You will create views based on queries from Lab 4 and rewrite the same queries with the views. You will do all these in a \texttt{Java} or \texttt{Python} application, for which we provide skeleton code (\texttt{Lab\_9.java}) and \texttt{Python} (\texttt{Lab\_9.py}). While you have the freedom to choose which programming language you use, you have to completely implement the lab in one of the two languages.

The tasks you have to implement are the following:
\begin{enumerate}
\item Create a view \textit{V1(c\_custkey, c\_name, c\_address, c\_phone, c\_acctbal, c\_mktsegment, c\_comment, c\_nation, c\_region)} that appends the country and region name to every customer. Rewrite \texttt{Q1} from Lab 4 with view \texttt{V1}.

\item Create a view \textit{V2(s\_suppkey, s\_name, s\_address, s\_phone, s\_acctbal, s\_comment, s\_nation, s\_region)} that appends the country and region name to every supplier. Rewrite \texttt{Q2} from Lab 4 with view \texttt{V2}.

\item Rewrite \texttt{Q3} from Lab 4 with view \texttt{V1}.

\item Rewrite \texttt{Q4} from Lab 4 with view \texttt{V2}.

\item Create a view \textit{V5(o\_orderkey, o\_custkey, o\_orderstatus, o\_totalprice, o\_orderyear, o\_orderpriority, o\_clerk, o\_shippriority, o\_comment)} that replaces \texttt{o\_orderdate} with the year \texttt{o\_orderyear} and contains all the other attributes in \texttt{orders}. Rewrite \texttt{Q5} from Lab 4 with views \texttt{V1} and \texttt{V5}.

\item Rewrite \texttt{Q6} from Lab 4 with view \texttt{V5}.

\item Rewrite \texttt{Q7} from Lab 4 with views \texttt{V1} and \texttt{V5}.

\item Rewrite \texttt{Q8} from Lab 4 with views \texttt{V2} and \texttt{V5}.

\item Rewrite \texttt{Q9} from Lab 4 with views \texttt{V2} and \texttt{V5}.

\item Create a view \textit{V10(p\_type, avg\_discount)} that computes the average discount for every type of part. Rewrite \texttt{Q10} from Lab 4 with view \texttt{V10}.

\item Rewrite \texttt{Q11} from Lab 4 with view \texttt{V2}.

\item Rewrite \texttt{Q12} from Lab 4 with view \texttt{V2}.

\item Rewrite \texttt{Q13} from Lab 4 with views \texttt{V1} and \texttt{V2}.

\item Rewrite \texttt{Q14} from Lab 4 with views \texttt{V1} and \texttt{V2}.

\item Create two views \textit{V151(c\_custkey, c\_name, c\_nationkey, c\_acctbal)} and \textit{V152(s\_suppkey, s\_name, s\_nationkey, s\_acctbal)} that contain the customers and suppliers with negative balance, respectively. Rewrite \texttt{Q15} from Lab 4 with views \texttt{V151} and \texttt{V152}.
\end{enumerate}

In order to complete the lab you have to perform the following tasks:
\begin{enumerate}
\item Log in to your GitLab account.

\item Explore the folders and files in the Lab 9 repo.

\item Create a merge request for the \texttt{Instructions} issue. This is done from the \texttt{Issues} tab. The result of the merge request is a new branch that copies the files from \texttt{master}.

\item Clone the repo to your local machine or the remote lab machine. You can choose to directly clone the branch for the merge request, or the \texttt{master} and then checkout the merge request branch.

\item Write the \texttt{Java} code that implements the required functionality in the corresponding methods in file \texttt{Lab\_9.java}. If you use \texttt{Python}, you edit the file \texttt{Lab\_9.py}. This is the only file you have to edit. Moreover, you have to write code only in the specified methods/functions. There are 21 such methods/functions overall.

\item For your reference, we provide you the \texttt{SQL} statements for all the queries in Lab 4 in file \texttt{queries-lab-4.sql}.

\item You can check the correctness of your queries by executing the command \texttt{make run} in the terminal. You have to be in the main lab folder. The expected output is available in \texttt{results/x.res}, where \texttt{x} is the number of the query. The output produced by your code is available in \texttt{output/x.out}. They have to match exactly for every query, e.g., \texttt{1.res} has to match with \texttt{1.out}. For queries that require parameters, you can find their values in the files \texttt{input/x.in}.

\item Commit the changes to the code file and then push to the GitLab server.

\item Check the output of the pipeline under the \texttt{CI / CD} tab to see if your push has passed all the tests.
\end{enumerate}

The score for the lab is assigned based on passing the test cases and the commit/push history. The instructor and the TAs have access to the GitLab repos. Moreover, the \texttt{MOSS} plagiarism detection software will be run on all of your submissions.

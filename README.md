# SOFE4630U-MS2
# Milestone 2: Data Processing Service (Dataflow)

##  Repository: 
[https://github.com/GeorgeDaoud3/SOFE4630U-MS2.git](https://github.com/GeorgeDaoud3/SOFE4630U-MS2.git)

## Objective:
1. Get familiar with Dataflow.
2. Understand MapReduce patterns.
3. Run batch and Stream Processing examples over MNIST dataset.

## Dataflow and a Simple Map Reduce Example:
In this section, you will learn about Dataflow, MapReduce pattern, and a word count as a MapReduce example. 
1. Watch this video about [https://www.youtube.com/watch?v=KalJ0VuEM7s](Google Cloud Dataflow).
2. Watch this video about [https://www.youtube.com/watch?v=JZiM-NsdiJo](MapReduce concepts).
3. Read this article about [https://www.analyticsvidhya.com/blog/2022/05/an-introduction-to-mapreduce-with-a-word-count-example/](implementing a word count example using the MapReduce patterns).

## Configure Dataflow
1. Open the GCP site.
2. Search for **Dataflow API**.
    
    ![](images/df1.jpg)
3. Then click **Enable** and Wait until the GCP get the service enabled for you.
  
  ![](images/df2.jpg)

4. To grant privileges for you project to use Dataflow, search for **Service Accounts**.
  
  ![](images/df3.jpg)

5. Create a new service account.

  ![](images/df4.jpg)

6. As the service name is a global identifier, it’s a good practice to use the project id as a prefix as **ProjectID-DFSA**, the project ID can be copied from the console.

  ![](images/df5.jpg)

7. Add **Compute Engine Service Agent**  and **Pub/Sub Admin** as roles to the service account.
  
  ![](images/df6.jpg)
  
8. Now, it’s time to install the python library of DataFlow
  ``` cmd
pip install pip --upgrade
pip install 'apache-beam[gcp]'
  ```

## Running the wordcount Example
1.	There already a set of examples exist within the python library folder. The following command will search for the wordcount within any subdirectory of the home directory (**~**) and print it.
  ``` cmd
find ~ -name 'wordcount.py'
  ```
  
2.	The following command will copy the file to the home directory (Replace path with the path you got from the previous step).
  ``` cmd
cp path  ~/wordcount.py
  ```
  Open the file using the text editor. Now, let’s try to understand the python code.
3.	The user can send arguments to customize the processing. The first step is to parse those arguments. Lines 69 to 73 define the first argument which will be set using the option **--input** . It’s an optional argument and if not given, it will have the default value given in line 72. The second argument is set using --output option. It’s required (not optional) and thus, no default value is needed. After describing the arguments, line 79 will parse the arguments and return a dictionary (known_args) with two keys named as the dest parameter of the parsed arguments (input and output)   



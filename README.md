# **Dockerized Mini ETL Pipeline**

This project is a simple, containerized ETL (Extract, Transform, Load) pipeline.

It uses Python and Pandas to read data from a CSV file, clean it, and then load the processed data into a SQLite database. The entire process is containerized using Docker.

## **Project Structure**

```
ETL Pipeline/
├── app/
│   ├── pipeline.py       # The main Python script for ETL
│   └── requirements.txt  # Python dependencies (pandas)
├── data/
│   ├── raw_data.csv      # Source data to be processed
│   └── (cleaned_data.db) # Generated database (not tracked by Git)
├── Dockerfile            # Instructions to build the Docker image
└── README.md             # This file
```

## **Prerequisites**

* [Docker](https://www.docker.com/get-started) must be installed and running.

## **How to Use**

### **1. Build the Docker Image**

From the root of the project directory (where the Dockerfile is), run:

```bash
docker build -t etl-pipeline .
```

### **2. Run the ETL Pipeline**

The Docker image is configured to run the Python script by default when a container is started.

```bash
docker run --name etl-container etl-pipeline
```

You will see the output in your terminal as the script executes:

```
✅ Extraction complete
✅ Transformation complete
✅ Load complete — data saved to SQLite
🎉 ETL Pipeline executed successfully!
```

The container will stop after the script finishes. The processed data is stored inside the container's volume.

### **3. (Optional) Run Interactively & Verify Data**

If you want to explore the container's shell and manually verify the data in the SQLite database, run the container in interactive mode:

1. **Start the container with a bash shell:**

   ```bash
   docker run -it --name etl-container-interactive etl-pipeline /bin/bash
   ```

   *Note: Using a new name like `etl-container-interactive` avoids conflicts if you ran the default command earlier.*

2. **Run the pipeline manually (if needed):**

   If you just want to explore, the default CMD won't have run. You can run the pipeline inside the container:

   ```bash
   root@container_id:/app# python app/pipeline.py
   ```

3. **Inspect the SQLite Database:**

   The pipeline saves the database to `/data/cleaned_data.db`. You can use the `sqlite3` CLI (which we installed in the Dockerfile) to inspect it.

   ```bash
   root@container_id:/app# sqlite3 /data/cleaned_data.db
   ```

4. **Query the data:**

   Once inside the SQLite shell, you can run commands:

   ```sql
   -- List tables
   .tables
   -- Output should be 'people'

   -- View the data
   SELECT * FROM people;

   -- Exit the sqlite shell
   .exit
   ```

5. **Exit the container:**

   When you are finished, type `exit` to stop and exit the container.

## **Features**

- **Containerized**: Fully Dockerized for easy deployment and portability
- **ETL Process**: Complete Extract, Transform, Load workflow
- **Data Cleaning**: Automated data transformation using Pandas
- **SQLite Storage**: Persistent data storage in SQLite database
- **Interactive Mode**: Optional shell access for debugging and verification

## **Technologies Used**

- **Python 3.x**: Core programming language
- **Pandas**: Data manipulation and transformation
- **SQLite3**: Lightweight database for data storage
- **Docker**: Containerization platform

## **Contributing**

Feel free to fork this repository and submit pull requests for any improvements.

## **License**

This project is open source and available under the MIT License.
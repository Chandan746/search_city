<h1>Search City</h1>
Migrate the data present in a remote MongoDB to local SQLite Django and
create REST API endpoints for them
<h2>Prerequisites</h2>
Python 3+ <br>

<h2>Installing</h2>
A step by step series of examples that tell you how to get a development env running.<br>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Migrating the data to local SQLite</h2>
Steps to create Db and database schema.
<pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

Steps to dump and load the data from remote MongoDB
<pre><code>python manage.py dbmigrate 'HOST ID' 'PORT' 'DB NAME' 'USERNAME' 'PASSWORD'</code></pre>
<h2>Create SuperUser</h2>
<pre><code>python manage.py createsuperuser</code></pre>

<h2>Running the project</h2>
<pre><code>python manage.py runserver</code></pre>

<h2>Input URL format </h2>
<pre><code>http://localhost/:8000/geo/search/&ltcountry_name&gt/&ltquery&gt/
</code></pre>

<pre><code>http://localhost/:8000/sectors/&ltmongo_sector_id&gt/
</code></pre>

<h2>Output JSON format </h2>
<pre><code>[
    {
        "id": City ID,
        "country_id": "Country ID",
        "name": "City Name"
    },
]
</code></pre>
<pre><code>[
    {
        "id": SubSector ID,
        "sector_id": "Sector ID",
        "name": "SubSector Name"
    },
]
</code></pre>

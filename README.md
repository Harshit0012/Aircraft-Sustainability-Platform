# Aircraft-Sustainability-Platform
Developed a platform linking aircraft makers, airlines, recycling units for efficient end-of-life aircraft component repurposing. Employed ML algorithms and data manipulation for optimal part reuse, recycling, and disposal decisions.


<h2>File Structure</h2>
<ul>
  <li>Project.zip</li>
  <ul>
  <li>Aerothon</li>
    <ul>
      <li>app</li>
      <li>data</li>
      <li>data_ingestion</li>
      <li>frontend</li>
      <li>requirement.txt</a></li>
  </ul>
</ul>
</ul>

<h2>Requirements </h2>
<ul>
  <li>Live Server ( to host frontend)</li>
  <li>Uvicorn ( to run API)</li>
  <li>Python 3</li>
  <li>Install all pip requirements (requirement.txt)</li>
</ul>


<h2>Setup</h2>

<h4>After fulfilling all requirements</h4>

<ul>
  <li>Turn on live server to host front end</li>
  <li>Run uvicorn to host api</li>
  <code>(powershell or gitbash) Pwd : ‘\Aerothon’

Command:
	#  uvicorn app.main:app --reload
If database is not created already hit any API to created database
    </code>
</ul>

	
We implemented database in MySQL but for prototype we also created SQLite Database with data ingestion

To insert data from excel please run the data ingestion file after define the structure (step 3) 
Run the data ingestion to push all excel data into database

<strong><a href="https://docs.google.com/document/d/1KoRptbmsZqsTzyUJpf-s8w5kkR4fDj4dHH5sLuFSIwE/edit?usp=sharing">full description about project</a></strong>

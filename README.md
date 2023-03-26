# Scheduling
* This work is the management and execution of back end database for the RoTF ordering and serving system.<br>
* The website framework is based on 'Flask' and Database Management System is 'MySql'.<br>
* There are three tables in a single database-<br><br>
1.Ordered - contains the columns<br><br>
<img width="429" alt="image" src="https://user-images.githubusercontent.com/109818534/227788259-d12b1712-2fbd-4975-99f8-56201e6fb368.png"><br>
<img width="496" alt="image" src="https://user-images.githubusercontent.com/109818534/227791112-b0265fdb-c083-4fb4-bb6d-0e3f31e85c6e.png">
<br>
* the entires are old and I am lazy to update them ;)<br>
* order_no is the unique key and must be kept uniqe while entering new data for order.<br>
* Order Name and ID can be selected with the table in 'over-coded' form.html which appears at home page : form.html needs update<br>
<br><br>
2.Kitchen -the columns are <br><br><img width="444" alt="image" src="https://user-images.githubusercontent.com/109818534/227788561-70dd1db2-330f-4c2c-b442-2b9481a9c2bf.png"><br><img width="403" alt="image" src="https://user-images.githubusercontent.com/109818534/227791155-f2108af3-c387-4a22-9268-ddc3981b1e35.png">
<br>
* this database is dispayed at the kitchen and the chef can select items whcih are prep<br>
<br><br>
3.Scheduled - the columns are <br><br><img width="604" alt="image" src="https://user-images.githubusercontent.com/109818534/227788617-d65287ab-84e5-4596-a804-a41d8210803a.png"><br><img width="418" alt="image" src="https://user-images.githubusercontent.com/109818534/227791216-91f94a8a-a37d-4894-9022-1e7be1bb2736.png">
<br>
<br>
* When the virtual env is created the first page that appears is '/' which is form.html. Users can enter their order here by giving a unique order no.(which ideally should be maintained internally and kept unique.). <br>
* After entring the order, we are redirectred to same page again and can order again.<br>
other pages are-<br><br>
<strong>/ordered</strong>
-this page dispays the entire ordered table which contains all the orders <br><br>
/kitchen - this page dispays the kitchen table which contains all the pending orders that are to be made including the OrderTime. This can be dispayed in the kitchen are.<br><br>
<strong>/delete</strong> - this page is accessible to the chef. It contains the kitchen table and a order no. entry form. The order prepared and ready to be served is enterd and is deleted form the kitchen table. The page is redirected to itself after the entry. form2.html is used here.<br><br>
<strong>/scheduled</strong> - this page displays the scheduled table whcih contains the WaitingTime. waiting time for a dish is the time it is left unserved after it is prepared.The priority order of serving is decided on basis of the waiting time.<br><br>

The priority information can further be used by the networking team to command the RoTF to carry out the respective orders in their priority order.
<br><br>
SIDE NOTE-<br>
* The database needs to be created on the host computer and database details can be modified at the top of code.
* For better functioning a free online database can be used for the RoTF .

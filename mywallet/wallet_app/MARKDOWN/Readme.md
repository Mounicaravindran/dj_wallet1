Wallet project

**MODELS:**

Used to store information about a users wallet in a database .

There are two fields namely is_active and balance

is_active: boolean field which is true by default

balance: decimal field that stores current balance of the wallet.

**SERIALIZER:**
 
 The meta class within the walletserializer is to provide metadata to the serializer

 The meta attribute has two fields which are model and fields

 model : specifies the model that the serializer should use for serialization and deserialization

 fileds: specifies which field should be included in the serialized/deserialized output

 **VIEWS:**

 It defines various views for django rest framework API which allows to create and manage wallet

 **WalletCreateView :** It is used to create new wallet objects

 It inherits from 'generics.CreateAPIView' which provides a default implementation for creating objects using the POST method

 sets queryset to all wallet objects

 **WalletActivateView:** It is used to activate wallet.


 Inherits from 'generics.UpdateAPIView' which update objects using PUT method

 Overrides the update method ,that is called when an update request is received

 In this method,it retrives the wallet object to be updated 

 Sets its is_active attribute to TRUE,saves the object and returns the serialized data.

 **WalletDisableView**: Same as WalletActivateView but sets is_active to FALSE.

 **WalletAddMoneyView:** Updates the balance attribute of the wallet

 It retrives the  amount of money to add from the request data, adds it to the balance attribute,saves the object and returns the serialized data.

 **WalletWithdrawMoneyView:** It subtracts the requested amount of money from the balance attribute of the wallet.

 **URLs:**

 Include and path are used to define the URL patterns in Django

It imports the path function from django's urls module and views defined in the 'views.py'.

The first path maps the URL to the WalletCreateView class and the following paths are mapped to the corresponding classes in the view.

The name parameter gives a name to the URL pattern to refer it in the other parts.

The path function takes two parameters a string and the include() function

String is used to represent a url pattern and a view to handle rquests.

The include() function is used to include the 'wallet.urls' in the URL patterns.

 

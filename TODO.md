

# todo

~~- research keyboard types~~
~~- support keyboards~~

- identify current user/order state?
- 
~~- design order flow~~

- review payment flow
- design router flow (menu, order, payment)
- design payment flow
- continue order flow



# database
 - users
 - orders
 - locations
 - items by location
 - packages by item id
 - delivery by item id
 - payments

# flow

 - get locations:
   - get available locations from DB
   - generate inline keyboard

 - get items:
   - get available items by location from DB
   - generate inline keyboard

 - order:
    - TO USER: 
      - get locations
      - send location list
      
    - FROM USER:
      - receive location from user 
      
    - TO USER: 
      ~~- create order (tmp)~~
      ~~- toggle order state ?~~
      - get items by location
      - send user the available items
      
    - FROM USER:
      - get item id

    - TO USER:
      ~~- toggle order state~~
      - get package type by item id (generic)
      - send user the package option items

    - FROM USER:
      - get package id

    - TO USER:
      ~~- toggle order state~~ 
      - get delivery type by item id (generic)
      - send user the delivery option items
    
    - FROM USER:
      - get delivery id  
 
    - TO USER:
      ~~- toggle order state~~
      - get available payment methods from db
      - send user the payment methods
      
    - FROM USER:
      ~~- get the payment method id~~

    - TO USER:
      - create order
      - toggle order state 
      - create new payment
      - toggle payment state
      - return INSTRUCTIONS (STEP 1)
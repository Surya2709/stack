# stackA stack is a basic data structure that can be logically thought of as a linear structure represented by a real physical stack or pile, a structure where insertion and deletion of items takes place at one end called top of the stack. The basic concept can be illustrated by thinking of your data set as a stack of plates or books where you can only take the top item off the stack in order to remove things from it. This structure is used all throughout programming.

The basic implementation of a stack is also called a LIFO (Last In First Out) to demonstrate the way it accesses data, since as we will see there are various variations of stack implementations.

There are basically three operations that can be performed on stacks. They are 1) inserting an item into a stack (push). 2) deleting an item from the stack (pop). 3) displaying the contents of the stack (peek or top). 


Stack<item-type> Operations

push(new-item:item-type)
    Adds an item onto the stack.
top():item-type
    Returns the last item pushed onto the stack.
pop()
    Removes the most-recently-pushed item from the stack.
is-empty():Boolean
    True if no more items can be popped and there is no top item.
is-full():Boolean
    True if no more items can be pushed.
get-size():Integer
    Returns the number of elements on the stack.

All operations except get-size() can be performed in O ( 1 ) {\displaystyle O(1)} O(1) time. get-size() runs in at worst O ( N ) . {\displaystyle O(N).} O(N).
Linked List Implementation

The basic linked list implementation is one of the easiest stack implementations you can do. Structurally it is a linked list.

type Stack<item_type>
  data list:Singly Linked List<item_type>
"stack follows the LIFO (last in first out) operation"
"queue follows the FIFO (first in first out) operation"
  constructor()
    list := new Singly-Linked-List()
  end constructor

Most operations are implemented by passing them through to the underlying linked list. When you want to push something onto the list, you simply add it to the front of the linked list. The previous top is then "next" from the item being added and the list's front pointer points to the new item.

  method push(new_item:item_type)
    list.prepend(new_item)
  end method

To look at the top item, you just examine the first item in the linked list.

  method top():item_type
    return list.get-begin().get-value()
  end method

When you want to pop something off the list, simply remove the first item from the linked list.

  method pop()
    list.remove-first()
  end method

A check for emptiness is easy. Just check if the list is empty.

  method is-empty():Boolean
    return list.is-empty()
  end method

A check for full is simple. Linked lists are considered to be limitless in size.

  method is-full():Boolean
    return False
  end method

A check for the size is again passed through to the list.

  method get-size():Integer
    return list.get-size()
  end method
end type

# Containers: 

These are classes that hold objects of a certain type. Examples include vectors, lists, maps, sets, etc.

## Pairs

## `std::pair` in C++

In C++, `std::pair` is a template class defined in the `<utility>` header. It is a simple container that can hold two heterogeneous objects as a single entity. `std::pair` is commonly used to return two values from a function or to store key-value pairs in associative containers like `std::map` and `std::unordered_map`. Here's an overview of `std::pair`:

1. **Template Class**:
   - `std::pair` is a template class that takes two template parameters: `T1` and `T2`. These parameters define the types of the first and second elements of the pair, respectively.
   - It can hold objects of any type, including built-in types, user-defined types, pointers, etc.

2. **Constructor**:
   - `std::pair` has a constructor that allows initializing the first and second elements of the pair.
   ```cpp
   std::pair<int, std::string> myPair(42, "Hello");
   ```

3. **Utility Functions**:
   - `std::make_pair(`: Creates a `std::pair` object with the provided values, deducing the types automatically.
   Can use myPair = {1,2};// For initialization
   ```cpp
   auto myPair = std::make_pair(42, "Hello");
   ```
   - std::tie(): Extracts the elements of a pair into separate variables.
   ```cpp
   int num;
   std::string str;
   std::tie(num, str) = myPair;
   ```

## Types of Containers: 


1. **Sequence Containers**:
   Sequence containers are data structures that store elements in a linear sequence. They maintain the order in which elements are inserted, allowing for sequential access to elements. Examples include:
   - **vector**: Dynamic array that allows random access.
   - **list**: Doubly linked list providing efficient insertion/deletion anywhere in the container.
   - **deque**: Double-ended queue allowing fast insertion/deletion at both ends.
   - **array**: Fixed-size array with a size determined at compile time.
   - **forward_list**: Singly linked list similar to `list`, but with forward-only iteration.

2. **Associative Containers**:
   Associative containers store elements in a sorted order based on keys. They provide fast retrieval based on keys. Examples include:
   - **set**: Collection of unique keys sorted in ascending order.
   - **map**: Collection of key-value pairs sorted by keys.
   - **multiset**: Allows duplicate keys in a sorted order.
   - **multimap**: Allows duplicate keys with key-value pairs sorted by keys.

3. **Unordered Containers**:
   Unordered containers store elements in an unordered manner using hash tables, offering fast insertion, deletion, and lookup operations. Examples include:
   - **unordered_set**: Collection of unique elements with no particular order.
   - **unordered_map**: Collection of key-value pairs with no particular order.
   - **unordered_multiset**: Allows duplicate elements with no particular order.
   - **unordered_multimap**: Allows duplicate keys with key-value pairs having no particular order.

4. **Container Adapters**:
   Container adapters provide a restricted interface to sequence containers. They adapt the underlying sequence container to provide a specific interface. Examples include:
   - **stack**: Provides a LIFO (Last In, First Out) data structure using a sequence container like `deque`, `list`, or `vector`.
   - **queue**: Provides a FIFO (First In, First Out) data structure using a sequence container like `deque` or `list`.
   - **priority_queue**: Provides a priority queue data structure using a sequence container like `vector`, with elements ordered by priority.

These categories help classify the various container types based on their underlying data structure and the operations they support.
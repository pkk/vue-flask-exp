<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Books</h1>
                <hr><br><br>
                <button class="btn btn-success btn-sm">Add Book</button>
                <br><br>
                <table class="table table-hove">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                            <th scope="col">Author</th>
                            <th scope="col">Read?</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(book,index) in books" :key="index">
                            <td>{{ book.title }}</td>
                            <td>{{ book.Author }}</td>
                            <td>
                                <span v-if="book.read">Yes</span>
                                <span v-else>No</span>
                            </td>
                            <td>
                                <div class="btn-group" role="group">
                                    <button class="btn btn-warning btn-sm">Update</button>
                                    <button class="btn btn-warning btn-sm">Delete</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            books: []
        };
    },
    methods: {
        getBooks() {
            const path = 'http://localhost:5000/books';
            axios.get(path)
            .then((res) => {
                this.books = res.data.books;
            })
            .catch((error) => {
                console.log(error);
            });
        },
    },
    created() {
        this.getBooks();
    },
};
</script>

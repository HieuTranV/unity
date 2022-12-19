<template>
  <h1>Total mails: {{ total_mail }}</h1>
  <h1>New mails this month: {{ new_mail_this_month }}</h1>
  <a-table
    class="ant-table-striped"
    size="middle"
    :columns="columns"
    :data-source="datas"
    :row-class-name="(_record, index) => (index % 2 === 1 ? 'table-striped' : null)"
    bordered
  />

  <a-button type="primary" @click="fetchData">Fetch</a-button>
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data() {
    return {
      datas: [],
      columns: [],
      total_mail: 0,
      new_mail_this_month: 0,
    };
  },
  mounted() {
    this.columns = [
      { title: "Email", dataIndex: "name" },
      { title: "Active", dataIndex: "is_active" },
      { title: "Subscribe", dataIndex: "is_subscribe" },
      { title: "Last Update", dataIndex: "last_update_timestamp", sorter: true, },
    ];
    this.datas = [];
    this.total_mail = 0;
    this.new_mail_this_month = 0;
    this.fetchData()
  },
  methods: {
    async fetchData() {
      axios
        .get(
          "http://localhost:8000/mail_management/get_list_mail/?partner_id=1"
        )
        .then((res) => {
          res.data.forEach((data) => {
            data.is_active = data.is_active ? "True" : "False";
            data.is_subscribe = data.is_subscribe ? "True" : "False";
          });
          this.datas = res.data;
        });

        axios
        .get(
          "http://localhost:8000/mail_management/get_number_mail/?partner_id=1"
        )
        .then((res) => {
          this.total_mail = res.data;
        });

        axios
        .get(
          "http://localhost:8000/mail_management/get_number_new_mail/?partner_id=1"
        )
        .then((res) => {
          this.new_mail_this_month = res.data;
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

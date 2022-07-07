<template>
  <div>
           <el-row justify="center" align="middle"
        ><el-col class="user-list">用户列表   <i class="iconfont icon-yonghu" style="font-size: 27px"></i></el-col></el-row
      >
            <el-divider></el-divider>
      <el-input placeholder="请输入要搜索的用户名" v-model="search" clearable>
      </el-input>
      <el-button type="primary" style="margin-left: 20px" @click="searchUser"
        >搜索</el-button
      >
      <el-button type="danger" style="margin-left: 20px" @click="shutDown"
        >关闭搜索结果</el-button
      >
      <div class="search-answer" v-if="isShowSearch">
        <p>搜索结果</p>
        <el-empty
          :image-size="100"
          v-if="this.searchData.length == 0"
        ></el-empty>
        <div class="search-box">
          <el-table
            :data="searchData"
            class="search"
            style="width: 100%"
            :row-style="{ height: '100px' }"
          >
            <el-table-column type="selection"> </el-table-column>
            <el-table-column label="uid">
              <template v-slot="scope">{{ scope.row.id }}</template>
            </el-table-column>
            <el-table-column prop="name" label="用户名">
              <template v-slot="scope">{{ scope.row.username }}</template>
            </el-table-column>
            <el-table-column prop="name" label="最后登录时间">
              <template v-slot="scope">{{ scope.row.update_at }}</template>
            </el-table-column>
            <el-table-column prop="name" label="邮箱">
              <template v-slot="scope">{{ scope.row.email }}</template>
            </el-table-column>
            <el-table-column label="操作">
              <template v-slot="scope">
                <el-button size="default" type="danger" @click="deleteOneUser(scope.row)"
                  >删除用户</el-button
                >
                <el-button
                  size="default"
                  type="primary"
                  @click="changeUsers(scope.row.username, scope.row.password,scope.row.id)"
                  >修改密码</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>
  <el-table
        ref="multipleTable"
        :data="tableData"
        tooltip-effect="dark"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection"> </el-table-column>
        <el-table-column label="uid">
          <template v-slot="scope">{{ scope.row.id }}</template>
        </el-table-column>
        <el-table-column prop="name" label="用户名">
          <template v-slot="scope">{{ scope.row.username }}</template>
        </el-table-column>
        <el-table-column prop="name" label="最后登录时间">
          <template v-slot="scope">{{ scope.row.update_at }}</template>
        </el-table-column>
        <el-table-column prop="name" label="邮箱">
          <template v-slot="scope">{{ scope.row.email }}</template>
        </el-table-column>

        <el-table-column label="操作">
          <template v-slot="scope">
            <el-button
              size="default"
              type="danger"
              @click="deleteOneUser(scope.row)"
              >删除用户</el-button
            >
            <el-button
              size="default"
              type="primary"
              @click="
                changeUsers(
                  scope.row.username,
                  scope.row.password,
                  scope.row.id
                )
              "
              >修改密码</el-button
            >
          </template>
        </el-table-column>
      </el-table>
            <div style="margin-top: 20px">
        <el-button @click="toggleSelection(tableData)">全选</el-button>
        <el-button @click="toggleSelection()">取消选择</el-button>
        <el-button type="danger" @click="deleteMoreUsers">删除</el-button>
      </div>
      <el-row justify="center">
        <el-col :xs="24" :sm="24" :md="10" :lg="10" :xl="7">
          <el-pagination
            background
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :page-size="pageSize"
            layout="prev, pager, next, jumper"
            :total="total"
            :current-page="becurrentPage"
            @next-click="goNextPage"
            @prev-click="goPrePage"
          >
          </el-pagination>
        </el-col>
      </el-row>
         <el-dialog title="用户信息" v-model="dialogTableVisible">
      <el-row justify="center">
        <el-form :rules="rules" hide-required-asterisk :model="changedUser">
          <span>用户名：{{ this.placeHolder.username }}</span>
          <el-form-item
            label="密码"
            prop="password"
            style="margin-top: 40px; margin-bottom: 40px"
          >
            <el-input
              type="password"
              v-model="changedUser.newpassword"
              style="width: 100%"
            />
          </el-form-item>
          <el-button @click="this.dialogTableVisible = false">取消</el-button>
          <el-button type="primary" :disabled="!canSubmit" @click="goChangeUser"
            >确认</el-button
          >
        </el-form></el-row
      >
    </el-dialog>
  </div>
</template>

<script>
import { getUserList,  changeUser,deleteMore } from "@/api/backend.js";
import { showFullScreenLoading, hideFullScreenLoading } from "@/utils/loading";
export default {
  name: "userlist",
  data() {
    return {
      dialogTableVisible: false,
      isShowSearch: false,
      search: "",
      placeHolder: {
        password: "",
      },
      changedUser: {
        newpassword: "",
        userId: "",
      },
      delete: {
        userIds: [],
      },
      oneDelete:{userId:''},
      pageSize: 10,
      total: 0,
      becurrentPage: 1,
      tableData: [],
      searchData: [],
      multipleSelection: [],
      rules: {
        username: [{ required: true, message: "用户名必填", trigger: "blur" }],
        newpassword: [
          { required: true, message: "密码必填", trigger: "blur" },
          { min: 6, message: "密码至少为6位", trigger: "blur" },
        ],
      },
      passWordRules: /^\S{6,}$/,
    };
  },
  created() {
    this.getTabelInfo();
  },
  methods: {
    getUserList,
    changeUser,
    deleteMore,
    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    getTabelInfo() {
      showFullScreenLoading(".backend-box");
      this.getUserList(this.becurrentPage+1, 10).then((res) => {
        hideFullScreenLoading(".backend-box");
        this.total = res.data.count;
        this.tableData = res.data.data;
      
      });
    },
    goNextPage() {
      
      this.getTabelInfo();
    },
    goPrePage() {
      this.getTabelInfo();
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },

    handleSizeChange(val) {
      this.pageSize = val;
      //   this.getTabelInfo();
  
    },
    handleCurrentChange(val) {
      this.becurrentPage = val;
      this.getTabelInfo();
      
    },
    shutDown() {
      this.isShowSearch = false;
    },
    searchUser() {
      if (this.search.split(" ").join("").length == 0) {
        this.$message.error("请输入用户名搜索！");
      } else {
        this.isShowSearch = true;
        showFullScreenLoading(".search-box");
        this.getUserList(1, 10, this.search).then((res) => {
          hideFullScreenLoading(".search-box");
        
          this.searchData = res.data.data;
       
        });
      }
    },
    changeUsers(username, password, id) {
      this.changedUser.userId = id;
      this.placeHolder.username = username;
      this.placeHolder.password = "";
      this.dialogTableVisible = true;
    },
    goChangeUser() {
      if (!this.passWordRules.test(this.changedUser.newpassword)) {
        this.$message.error("格式错了哦,密码至少6位");
      } else {
        this.changeUser(this.changedUser);
        this.$message.success("更新成功！");
        this.dialogTableVisible = false;
      }
    },
    deleteOneUser(row) {
      this.$confirm("是否确定删除该用户?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.delete.userIds.push(row.id)
          showFullScreenLoading(".backend-box");
          this.deleteMore(this.delete).then((res) => {
            hideFullScreenLoading(".backend-box");
   
          });
          this.getTabelInfo();
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消操作",
          });
        });
    },
    deleteMoreUsers() {
      if (this.multipleSelection.length == 0) {
        this.$message.warning("请选择要删除的记录哦");
      } else {
        this.$confirm("此操作将永久删除, 是否继续?", "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        })
          .then(() => {
            showFullScreenLoading(".backend-box");
            this.delete.userIds = this.multipleSelection.map((item) => {
              return item.id;
            });
        
            this.deleteMore(this.delete).then((res) => {
              hideFullScreenLoading(".backend-box");
          
              this.getTabelInfo();
              this.tableData = this.tableData.filter((item) => {
                return this.multipleSelection.every((item2) => {
                  return item.id != item2.id;
                });
              });
              this.$message({
                type: "success",
                message: "删除成功!",
              });
            });
          })
          .catch(() => {
             hideFullScreenLoading(".backend-box");
            this.$message({
              type: "info",
              message: "已取消删除",
            });
          });
      }
    },
  },
  computed: {
    canSubmit() {
      const { newpassword } = this.changedUser;
      return Boolean(newpassword);
    },
  },

};
</script>

<style scoped>
* {
  font-family: SimHei sans-serif;
}
.el-header {
  text-align: center;
  font-size: 30px;
  line-height: 100px;
}
.backend-box {
  padding-right: 50px;
  padding-left: 50px;
}
.user-list {
  margin-bottom: 20px;
  font-size: 23px;
  text-align: center;
}
.el-pagination {
  text-align: center;
  margin: 20px 0 10px 0;
}
.el-input {
  width: 20%;
}
.search {
  color: red;
  font-size: 20px;
}
.search-answer {
  text-align: center;
  transition: all 0.5s;
}
</style>
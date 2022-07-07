<template>
  <div>
    <vue-particles
      color="#409EFF"
      :particleOpacity="0.7"
      :particlesNumber="60"
      shapeType="circle"
      :particleSize="6"
      linesColor="#409EFF"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.4"
      :linesDistance="150"
      :moveSpeed="4"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="true"
      clickMode="push"
    >
    </vue-particles>
    <MyHeader class="theheader"></MyHeader>
    <img src="@/assets/image/other/bg1.jpg" class="bg" />
    <div class="container1" id="container">
      <div class="form-container sign-up-container">
        <el-form
          class="login-form"
          label-width="60px"
          :model="user"
          :rules="rules"
          hide-required-asterisk
          @keyup.enter.native="createUser"
          ref="create"
        >
          <h1>注册</h1>
          <el-form-item
            label="用户名"
            style="align-items: center"
            prop="username"
          >
            <el-input v-model="user.username" placeholder="新用户的登录名" />
          </el-form-item>
          <el-form-item
            label="密码"
            style="align-items: center"
            prop="password"
          >
            <el-input
              type="password"
              v-model="user.password"
              placeholder="至少 ≥ 6 位"
            />
          </el-form-item>
          <el-form-item label="邮箱" style="align-items: center" prop="email">
            <el-input v-model="user.email" placeholder="您的邮箱" />
          </el-form-item>

          <el-button @click="createUser" :disabled="!canReg">创建</el-button>
        </el-form>
      </div>
      <div class="form-container sign-in-container">
        <el-form
          :rules="rules"
          @keyup.enter.native="gologin"
          hide-required-asterisk
          :model="user"
          ref="login"
          class="login-table"
        >
          <h1 id="login-title">请登录</h1>
          <el-form-item
            label="用户名"
            prop="username"
            style="align-items: center"
          >
            <el-input v-model="user.username" autofocus />
          </el-form-item>
          <el-form-item
            label="密码"
            prop="password"
            style="align-items: center; padding-left: 11.5px"
          >
            <el-input type="password" v-model="user.password" />
          </el-form-item>
          <p class="forget-psw" @click="goForget">忘记密码</p>
          <el-button @click="gologin" :disabled="!canSubmit">登录</el-button>
        </el-form>
        <el-form
          :rules="rules"
          @keyup.enter.native="gologin"
          hide-required-asterisk
          :model="forget"
          class="forget-table"
        >
          <h1>重设密码</h1>
          <el-form-item
            label="用户名"
            prop="username"
            style="align-items: center"
          >
            <el-input v-model="forget.username" autofocus />
          </el-form-item>
          <el-form-item
            label="您的邮箱"
            prop="myemail"
            style="align-items: center"
          >
            <el-input v-model="forget.myemail" autofocus />
          </el-form-item>
          <el-form-item
            label="新密码"
            prop="newPassword"
            style="align-items: center"
          >
            <el-input type="password" v-model="forget.newPassword" />
          </el-form-item>
          <p class="forget-psw" @click="goBackLogin">返回登录</p>
          <el-button :disabled="!canReset" @click="goReset">确认</el-button>
        </el-form>
      </div>

      <div class="overlay-container">
        <div class="overlay">
          <div class="overlay-panel overlay-left">
            <h1>已有账号？去登录</h1>

            <button class="ghost" @click="goSignIn">去登录</button>
          </div>
          <div class="overlay-panel overlay-right">
            <h1>没注册？去注册</h1>

            <button class="ghost" @click="goSignUp">去注册</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { create, login, reset } from "@/api/login";
import MyHeader from "@/components/MyHeader";
import bg from "@/assets/image/other/bg1.jpg";
export default {
  name: "login",
  components: {
    MyHeader,
  },
  data() {
    return {
      bg: bg,
      user: {
        username: "",
        password: "",
        email: "",
      },
      forget: {
        username: "",
        myemail: "",
        newPassword: "",
      },
      rules: {
        username: [{ required: true, message: "用户名必填", trigger: "blur" }],
        password: [
          { required: true, message: "密码必填", trigger: "blur" },
          { min: 6, message: "密码至少为6位", trigger: "blur" },
        ],
        email: [
          {
            required: true,
            message: "邮箱必填，用于找回密码",
            trigger: "blur",
          },
          {
            pattern: /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/,
            message: "邮箱格式错误",
            trigger: "blur",
          },
        ],
        myemail: [
          {
            required: true,
            message: "邮箱必填",
            trigger: "blur",
          },
          {
            pattern: /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/,
            message: "邮箱格式错误",
            trigger: "blur",
          },
        ],
        newPassword: [
          { required: true, message: "密码必填", trigger: "blur" },
          { min: 6, message: "密码至少为6位", trigger: "blur" },
        ],
      },
      passWordRules: /^\S{6,}$/,
      emailRules: /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/,
    };
  },
  mounted() {
    document.body.style.overflowX = "hidden";
  },
  computed: {
    canSubmit() {
      const { username, password } = this.user;
      return Boolean(username && password);
    },
    canReset() {
      const { username, newPassword, myemail } = this.forget;
      return Boolean(username && newPassword && myemail);
    },
    canReg() {
      const { username, password, email } = this.user;
      return Boolean(username && password && email);
    },
  },
  methods: {
    gologin() {
      login(this.user)
        .then(({ data }) => {
      
          if (data.code == 1) {
            this.$message.error(data.msg);
          } else {
        
            const { accessToken } = data.data;
            const { superAdmin } = data.data;
            localStorage.setItem("token", accessToken);
            localStorage.setItem("superAdmin", superAdmin);
            if (superAdmin == "admin") {
              this.$router.push("userlist");
            } else {
              this.$router.push("detectchanges");
              this.$message.success("登录成功！");
            }
          }
        })
        .catch((err) => {
          this.$message.error(err.response.data.message);
        });
    },
    createUser() {
      if (!this.passWordRules.test(this.user.password)) {
        this.$message.error("格式错了哦,密码至少6位");
      } else if (!this.emailRules.test(this.user.email)) {
        this.$message.error("邮箱格式错误了哦");
      } else {
        create(this.user).then((res) => {
          if (res.data.code == 1) {
            this.$message.error(res.data.msg);
            this.user = { username: "", password: "", email: "" };
          } else {
            this.goSignIn();
            this.$message.success("创建成功");
            this.user = { username: "", password: "", email: "" };
          }
        });
      }
    },
    goReset() {
      if (!this.passWordRules.test(this.forget.newPassword)) {
        this.$message.error("格式错了哦,密码至少6位");
      } else if (!this.emailRules.test(this.forget.myemail)) {
        this.$message.error("邮箱格式错误了哦");
      } else {
        reset(this.forget).then((res) => {
        
          if (res.data.code == 1) {
            this.$message.error(res.data.msg);
            this.forget = { username: "", newPassword: "", myemail: "" };
          } else {
            this.$message.success("重置成功");
            this.forget = { username: "", newPassword: "", myemail: "" };
          }
        });
      }
    },
    goSignUp() {
      let container = document.getElementById("container");
      container.classList.add("right-panel-active");
    },
    goSignIn() {
      let container = document.getElementById("container");
      container.classList.remove("right-panel-active");
    },
    goForget() {
      this.user = { username: "", password: "" };
      document.querySelector(".login-table").classList.add("active-login");
      document.querySelector(".forget-table").classList.add("active-forget");
    },
    goBackLogin() {
      this.user = { username: "", password: "" };
      document.querySelector(".login-table").classList.remove("active-login");
      document.querySelector(".forget-table").classList.remove("active-forget");
    },
  },
};
</script>

<style scoped>
body {
  overflow-x: hidden;
}
#particles-js {
  width: 100%;
  height: calc(100% - 100px);
  position: absolute;
  top: 0;
  left: 0;
}
.theheader {
  height: 0px;
  color: skyblue;
}
.bg {
  z-index: -1;
  height: 100%;
  background-size: 100%;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;

  background-size: cover;
}
.container1 {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  position: absolute;
  overflow: hidden;
  width: 50vw;
  height: 40vh;
  max-width: 100%;
  min-width: 500px;
  min-height: 480px;
  left: 0;
  right: 0;

  top: 21vh;
  margin: auto;
  opacity: 0.7;
}
.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}
.sign-in-container {
  left: 0;
  width: 50%;
  z-index: 2;
}
.container1.right-panel-active .sign-in-container {
  transform: translateX(100%);
}
.sign-up-container {
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}
.container1.right-panel-active .sign-up-container {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: show 0.41s;
}
.login-table {
  transition: all 0.7s;
}
.forget-table {
  transition: all 0.7s;
  opacity: 0;
}
.active-login {
  opacity: 0;
  z-index: -1;
}
.active-forget {
  transform: translateY(-100%);
  opacity: 1;
}
@keyframes show {
  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }

  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
}

.overlay-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}

.container1.right-panel-active .overlay-container {
  transform: translateX(-100%);
}

.overlay {
  background: skyblue;
  background: -webkit-linear-gradient(to right, skyblue, #ff416c);
  background: linear-gradient(to right, skyblue, skyblue);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 0 0;
  color: #ffffff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.container1.right-panel-active .overlay {
  transform: translateX(50%);
}

.overlay-panel {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 40px;
  text-align: center;
  top: 0;
  height: 100%;
  width: 50%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.overlay-left {
  transform: translateX(-20%);
}

.container1.right-panel-active .overlay-left {
  transform: translateX(0);
}

.overlay-right {
  right: 0;
  transform: translateX(0);
}
.container1.right-panel-active .overlay-right {
  transform: translateX(20%);
}

* {
  box-sizing: border-box;
  font-family: "Montserrat", sans-serif;
}
.el-button {
  transition: all 0.4s;
}
button {
  border-radius: 20px;
  border: 1px solid skyblue;
  background-color: skyblue;
  color: #ffffff;
  font-size: 18px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin: 0 auto;
  transition: transform 80ms ease-in;
}

button:active {
  transform: scale(0.95);
}
button:focus {
  outline: none;
}
button.ghost {
  background-color: skyblue;
  border-color: #ffffff;
  cursor: pointer;
  transition: all 0.4s;
}
.ghost:hover {
  color: skyblue;
  background-color: white;
}

form {
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 50px;
  height: 100%;
  text-align: center;
}

input {
  border: none;
  padding: 12px 15px;
  margin: 8px 0;
  width: 100%;
  background: rgb(209, 207, 208);
}
.forget-psw {
  color: skyblue;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.5s;
}
.forget-psw:hover {
  color: rgb(255, 145, 0);
}
.el-button {
  font-size: 16px;
}
</style>

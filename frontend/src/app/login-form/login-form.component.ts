import {Component, OnInit} from '@angular/core';
import { CategoryService } from '../category.service';
import { AuthService } from '../auth-service.service';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.css']
})
export class LoginFormComponent implements OnInit {
  logged = false;
  username = '';
  password = '';

  constructor(private AuthService:AuthService) {
  }

  ngOnInit(): void {
    let token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  reload(){
    window.location.reload
    window.location.href = "http://localhost:4200/home"
  }

  login(){
    this.AuthService.login(this.username, this.password)
    .subscribe(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;

        this.username = '';
        this.password = '';
        this.reload()
      }
    )

      
  }

  logout(){
    console.log(this.logged)
    localStorage.clear();
    this.logged = false;
    console.log(this.logged)
  }

}

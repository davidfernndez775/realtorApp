import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthServiceService {
  private baseUrl: string = 'http://127.0.0.1:8000/app/auth';
  private registerUrl: string = `${this.baseUrl}/register/`;
  constructor(private http: HttpClient) {}

  register() {}
}

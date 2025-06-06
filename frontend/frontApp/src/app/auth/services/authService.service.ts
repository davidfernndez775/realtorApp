import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AuthServiceService {
  private readonly baseUrl: string = environment.baseUrl;
  private registerUrl: string = `${this.baseUrl}/auth/register/`;
  constructor(private http: HttpClient) {}

  register() {}
}

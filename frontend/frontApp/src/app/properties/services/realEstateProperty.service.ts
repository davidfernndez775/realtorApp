import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {
  RealEstateProperty,
  RealEstatePropertyImages,
} from '../interfaces/realEstateProperty';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class RealEstatePropertyService {
  private baseUrl: string = 'http://127.0.0.1:8000/app/real-estate';
  private listUrl: string = `${this.baseUrl}/list/`;
  private imageUrl: string = `${this.baseUrl}/property-images`;
  constructor(private http: HttpClient) {}

  getPropertyList(filters?: any): Observable<RealEstateProperty[]> {
    let params = new HttpParams();
    if (filters) {
      Object.keys(filters).forEach((key) => {
        if (filters[key]) {
          params = params.set(key, filters[key]);
        }
      });
    }

    return this.http.get<RealEstateProperty[]>(this.listUrl, { params });
  }

  getPropertyImages(
    property: number
  ): Observable<RealEstatePropertyImages[] | null> {
    return this.http.get<RealEstatePropertyImages[]>(
      `${this.imageUrl}/?property=${property}`
    );
  }
}

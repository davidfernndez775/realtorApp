import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {
  RealEstateProperty,
  RealEstatePropertyImages,
} from '../interfaces/realEstatePropertyinterface.';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class RealEstatePropertyService {
  private readonly baseUrl: string = environment.baseUrl;
  private listUrl: string = `${this.baseUrl}/real-estate/list/`;
  private imageUrl: string = `${this.baseUrl}/real-estate/property-images`;
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
